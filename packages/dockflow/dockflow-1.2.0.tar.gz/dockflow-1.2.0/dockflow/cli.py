import click
import docker
import json
import os
from pathlib import Path
import subprocess 


default_composer_version = 'composer-2.9.8-airflow-2.9.3'
airflow_home = '/usr/local/airflow'

def cwd():
    return Path(os.getcwd())
    

def get_docker_client(): # pragma: no cover
    docker_client = docker.from_env()
    return docker_client


def network_handler(network:str, docker_client):
    if not docker_client.networks.list(filters={'name': network}):
        click.secho(f'"{network}" network does not exist. \n Creating...', fg='cyan')
        docker_client.networks.create(
            network,
            driver='bridge',
        )
        click.secho(f'"{network}" network created', fg='green')
    else:
        click.secho(f'"{network}" network already exists', fg='cyan')


def write_config():
    # Check whether config dir exists
    config_dir = Path.home() / '.dockflow'
    if dir_exist(config_dir) is False:
        os.mkdir(config_dir)
    # Prompt user for input
    image_repo = click.prompt(
        'Please enter your container repo URL',
    )
    # Write to config file
    config_file = Path.home() / '.dockflow' / 'dockflow.cfg'
    with open(config_file, 'w') as cfg:
        cfg.write(image_repo)
    click.secho(f'Container repo set to: {image_repo}', fg='green')


def check_config(config_file): # pragma: no cover
    filename = os.path.expanduser(config_file)
    filesize = os.path.getsize(filename)
    # If file is empty create config
    if filesize == 0: 
        write_config()

    with open(filename) as cfg:
        image_repo = cfg.read().strip('\r').strip('\n')
    return image_repo


def copy_to_docker(filename, container_name):
    local_path = str(Path(cwd() / filename))
    subprocess.run(['docker', 'cp', local_path, f'{container_name}:{airflow_home}/{filename}'], text=True)


def dir_exist(directory): # pragma: no cover
    return os.path.exists(directory)


def prefix(directory):
    last_path = os.path.split(directory)
    container_prefix = last_path[1]
    return container_prefix


def ask_user(question): # pragma: no cover
    check = str(input(question + '(Y/N): ')).lower().strip()
    try:
        if check[0] == 'y':
            return True
        elif check[0] == 'n':
            return False
        else:
            print('Invalid Input')
            return ask_user(question)
    except Exception as error:
        print('Please enter valid inputs')
        print(error)
        return ask_user(question)


@click.group()
def main(): # pragma: no cover
    """
        Spatialedge Airflow Development CLI \n
    """
    pass


@main.command()
@click.option(
    '-iv',
    '--image-version',
    help='Specify Cloud Composer Airflow version',
    type=str,
    default=default_composer_version,
)
@click.option(
    '--config-file',
    '-c',
    type=click.Path(),
    default='~/.dockflow/dockflow.cfg',
)
@click.option(
    '--gcp-creds',
    '-creds',
    type=click.Path(),
    default= Path.home() / ".config" / "gcloud" / "application_default_credentials.json"
)
@click.option(
    '--network',
    '-net',
    type=str,
    default='dockflow'
)
@click.option(    
    '--check-images',
    '-ci',
    help='Check available Airflow images and allow selection.',
    is_flag=True,
)
def start(image_version, config_file, gcp_creds, network, check_images):
    """
        Start Airflow instance
    """
    image_repo = check_config(config_file)
    docker_client = get_docker_client()

    is_image_version_provided = image_version != default_composer_version

    volumes = {}

    if docker_client.containers.list(filters={'name': f'{prefix(cwd())}-airflow', 'status': 'created'}):
        click.secho(f'It seems that {prefix(cwd())}-airflow failed to start', fg='red')
        click.secho('Removing container and attempting to start', fg='red')
        container = docker_client.containers.get(f'{prefix(cwd())}-airflow')
        container.remove()

    click.secho(f'Checking if container {prefix(cwd())}-airflow is already running', fg='green')
    if docker_client.containers.list(filters={'name': f'{prefix(cwd())}-airflow', 'status': 'running'}):
        click.secho(f'Container {prefix(cwd())}-airflow already running', fg='green') # pragma: no cover
    elif docker_client.containers.list(filters={'name': f'{prefix(cwd())}-airflow', 'status': 'exited'}):
        if is_image_version_provided or check_images:
            click.secho(f"Container {prefix(cwd())}-airflow already exists. Remove container AND existing airflow.db if you would like to use a different image.", fg="yellow")
            click.secho(f"Starting existing container...", fg='green')
        container = docker_client.containers.get(f'{prefix(cwd())}-airflow')
        container.start()
        if dir_exist(cwd() / 'airflow.db'):
            copy_to_docker('airflow.db', f'{prefix(cwd())}-airflow')
            container.exec_run(f'chown airflow {airflow_home}/airflow.db', user='root')
        click.secho(f'Container {prefix(cwd())}-airflow started', fg='green', bold=True)

    else:
        try:
            click.secho("Fetching image data...", fg="green")
            images_data = get_available_images(image_repo)

            if check_images:
                image_version = select_image_from_list(images_data)
            elif not check_images:
                image_version = check_for_latest_image(images_data, image_version)

        except (subprocess.CalledProcessError, json.JSONDecodeError, Exception) as e:
            click.secho(f"Error handling images: {e}", fg="red")
            click.secho(f"Falling back to default image version: {default_composer_version}", fg="yellow")
            image_version = default_composer_version  # Revert to the default
        
        click.secho(f'Starting container {prefix(cwd())}-airflow:{image_version.strip("=")} creation', fg='green')

        version = image_version.strip('=')
        image_repo = check_config(config_file)
        click.secho('Checking if image is up-to-date...', fg='green')
        subprocess.run(['docker', 'pull', f'{image_repo}:{version}'], text=True)
        click.secho('Checking if "dags" folder exists', fg='green')
        if dir_exist(cwd() / 'dags/'):
            mount_loc = f'{airflow_home}/dags/'
            volumes[cwd() / 'dags/'] = {'bind': mount_loc, 'mode': 'rw'}
            click.secho(f'"dags" folder mounted to: {mount_loc}', fg='green')

            click.secho('Checking if "scripts" directory exists and mount if exist', fg='green')
            if dir_exist(cwd() / 'scripts/'):
                mount_loc = f'{airflow_home}/scripts/'
                volumes[cwd() / 'scripts/'] = {'bind': mount_loc, 'mode': 'rw'}
                click.secho(f'"scripts" directory mounted to {mount_loc}', fg='cyan')
            else: # pragma: no cover
                click.secho(f'"scripts" directory not found in: {cwd()} \n Not mounting', fg='red')

            click.secho(f'Checking if "{network}" network exists', fg='cyan')
            network_handler(network=network, docker_client=docker_client)

            container = docker_client.containers.create(
                image_repo + ':' + version,
                ports={'8080/tcp': 8080,
                       },
                volumes=volumes,
                network=network,
                name=f'{prefix(cwd())}-airflow',
                environment={
                    'GOOGLE_APPLICATION_CREDENTIALS': '/usr/local/airflow/gcp_credentials.json',
                    },
            )
            click.secho(f'Container {prefix(cwd())}-airflow:{version} created', fg='green')
            
            click.secho('Check if GCP credentials exist and mount if exists', fg='green')
            creds = os.path.expanduser(gcp_creds)
            if dir_exist(creds):
                click.secho(f'Mounting GCP credentials: {creds}', fg='cyan')
                subprocess.run(['docker', 'cp', f'{creds}', f'{prefix(cwd())}-airflow:{airflow_home}/gcp_credentials.json'], text=True)
            else: # pragma: no cover
                click.secho(f'GCP Credential file {creds} not found, will not mount to container', fg='red')

            container.start()

            if dir_exist(creds):
                container.exec_run("/bin/bash -c 'chmod 704 gcp_credentials.json'", user='root')
            click.secho('Check if local airflow.db exist and copy if exist', fg='green')
            if dir_exist(cwd() / 'airflow.db'):
                copy_to_docker('airflow.db', f'{prefix(cwd())}-airflow')
                container.exec_run(f'chown airflow {airflow_home}/airflow.db', user='root')
                click.secho('Local airflow.db mounted to container', fg='cyan')
            click.secho(f'Container {prefix(cwd())}-airflow:{version} started', fg='green', bold=True)
        else: # pragma: no cover
            click.secho('DAGs directory not found in: {} \nAre you in the root directory of your project?'.format(cwd()),
                        fg='red', bold=True)


@main.command()
@click.option(
    '--rm',
    is_flag=True
)
def stop(rm):
    """
        Stop Airflow instance
    """
    docker_client = get_docker_client()

    if docker_client.containers.list(filters={'name': f'{prefix(cwd())}-airflow'}):
        container = docker_client.containers.get(prefix(cwd()) + "-airflow")
        click.secho('Persisting Airflow db', fg='green')
        subprocess.run(['docker', 'cp', f'{prefix(cwd())}-airflow:{airflow_home}/airflow.db', f'{Path(cwd() / "airflow.db")}'], text=True)
        click.secho(f'"airflow.db" persisted to {Path(cwd() / "airflow.db")}', fg='cyan')
        click.secho(f'Stopping {prefix(cwd())}-airflow...', fg='red')
        container.stop()
        if rm:
            container.remove()
            click.secho(f'{prefix(cwd())}-airflow stopped and removed', fg='red')
        else:
            click.secho(f'{prefix(cwd())}-airflow stopped', fg='red')
    elif docker_client.containers.list(filters={'name': f'{prefix(cwd())}-airflow', 'status': 'exited'}) and rm:
        container = docker_client.containers.get(f'{prefix(cwd())}-airflow')
        container.remove()
        click.secho(f'{prefix(cwd())}-airflow removed', fg='red')
    else: # pragma: no cover
        click.secho('Nothing to stop.', fg='red')

@main.command()
def refresh():
    """
        Run refresh/bundling scripts
    """
    docker_client = get_docker_client()

    container = docker_client.containers.get(prefix(cwd()) + '-airflow')
    if dir_exist(cwd() / 'scripts/'):
        click.secho('Refreshing dags...', fg='green')
        for f in os.listdir(cwd() / 'scripts/'):
            script_path = f'{airflow_home}/scripts/{f}'
            container.exec_run(f'python "{str(script_path)}"', user='airflow')
        click.secho('All DAGs refreshed', fg='green')
    else: # pragma: no cover
        click.secho('Either not project root directory or no "scripts" folder present', fg='red')


@main.command()
def config(): # pragma: no cover
    """
        Store container repo URL
    """
    write_config()


@main.command()
def reset():
    """
        Reset Airflow db
    """
    docker_client = get_docker_client()

    container = docker_client.containers.get(f'{prefix(cwd())}-airflow')
    if ask_user('Are you sure?'):
        click.secho('Resetting Airflow database...', fg='green')
        container.exec_run('airflow resetdb -y')
        click.secho('Restarting container...', fg='green')
        container.stop()
        container.start()
        click.secho('Airflow db reset completed', fg='green')


@main.command()
def dashboard():# pragma: no cover
    """
        Open Airflow in default browser
    """
    click.launch('http://localhost:8080')


@main.command()
@click.option(
    '-iv',
    '--image-version',
    help='Specify Cloud Composer Airflow version',
    type=str,
    default=default_composer_version,
)
@click.option(
    '--config-file',
    '-c',
    type=click.Path(),
    default='~/.dockflow/dockflow.cfg',
)
def test(image_version, config_file):
    """
        Run tests located in tests dir if test.sh exists
    """
    docker_client = get_docker_client()

    click.secho(f'Creating volumes for {prefix(cwd())}-test', fg='green', bold=True)

    volumes = {}
    version = image_version.strip('=')
    image_repo = check_config(config_file)

    click.secho('Checking if required directories (dags & tests) exist', fg='green')
    if dir_exist(cwd() / 'dags/') and dir_exist(cwd() / 'tests/'):
        click.secho('Mounting "dags" directory', fg='green')
        volumes[cwd() / 'dags/'] = {'bind': f'{airflow_home}/dags/', 'mode': 'rw'}
        click.secho('"dags" directory mounted', fg='cyan')

        click.secho('Mounting "tests" directory', fg='green')
        volumes[cwd() / 'tests/'] = {'bind': f'{airflow_home}/tests/', 'mode': 'rw'}
        click.secho('"tests" directory mounted', fg='cyan')

        click.secho('Checking if "scripts" directory exists and mount if exist', fg='green')
        if dir_exist(cwd() / 'scripts/'):
            volumes[cwd() / 'scripts/'] = {'bind': f'{airflow_home}/scripts/', 'mode': 'rw'}
            click.secho('"scripts" directory mounted', fg='cyan')
        else:
            click.secho(f'"scripts" directory not found in: {cwd()} \n Not mounting', fg='red') # pragma: no cover

        click.secho('Creating {}-test'.format(prefix(cwd())), fg='green', bold=True)
        container = docker_client.containers.create(
            image_repo + ':' + version,
            volumes=volumes,
            name=prefix(cwd()) + '-test',
        )

        try:
            click.secho('Checking if required scripts exist', fg='green')
            if dir_exist(cwd() / 'test.sh'):
                copy_to_docker('test.sh', f'{prefix(cwd())}-test')
                container.start()
                container.exec_run(f'chown airflow {str(airflow_home)}/test.sh', user='root')
                container.exec_run(f'chmod +x {str(airflow_home)}/test.sh', user='root')

                # Bundle configs
                if dir_exist(cwd() / 'scripts/'):
                    click.secho('Refreshing DAGs...', fg='green')
                    for f in os.listdir(cwd() / 'scripts/'):
                        script_path = f'{airflow_home}/scripts/{f}'
                        container.exec_run(f'python "{str(script_path)}"', user='airflow')
                    click.secho('All DAGs refreshed', fg='green')
                else:
                    click.secho(f'Either not project root or no "scripts" folder present in: {cwd()}', fg='red') # pragma: no cover

                click.secho('Executing test.sh to run tests', fg='green', bold=True)
                subprocess.run(['docker', 'exec', f'{prefix(cwd())}-test', './test.sh'], text=True)
            else: # pragma: no cover
                click.secho('No test script found...', fg='red')
                click.secho('Ensure you are in the project root directory and `test.sh` exists', fg='red', bold=True)

        finally:
            click.secho(f'Stopping and removing container: {prefix(cwd())}-test', fg='red')
            container.stop()
            container.remove()
            click.secho(f'Container {prefix(cwd())}-test stopped and removed', fg='red', bold=True)
    else: # pragma: no cover
        click.secho(f'Required directories not found in: {cwd()}', fg='red', bold=True)


@main.command()
def requirements():
    """
    Create ide.requirements.txt
    """
    docker_client = get_docker_client()

    # Creates a file ide.requirements.txt in root dir of project matching current running container requirements
    if docker_client.containers.list(filters={'name': (prefix(cwd()) + '-airflow'), 'status': 'running'}):
        subprocess.run(['docker', 'exec', '-it', '-u', 'airflow', f'{prefix(cwd())}-airflow', 'pip', 'freeze', '>', 'ide.requirements.txt'], text=True)
    else: # pragma: no cover
        click.secho('Could not find a running container. Ensure you are in the root directory of your project')


def get_available_images(image_repo):
    """Fetches and sorts available images from the repository (newest to oldest).

    Args:
        image_repo (str): The repository URL to fetch images from.

    Returns:
        list: A list of dictionaries containing image data, sorted from newest to oldest.

    Raises:
        click.ClickException: If `gcloud` is not installed, or if there is an error executing the `gcloud` command, 
                              or if there is an error decoding the JSON response, or if an unexpected error occurs.
    """
    command = [
        "gcloud",
        "artifacts",
        "docker",
        "tags",
        "list",
        "--format=json",
        image_repo
    ]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        json_output = result.stdout
        images_data = json.loads(json_output)
 
        # Reverse the order of the JSON data to get newest to oldest
        images_data.reverse()

        return images_data
    except FileNotFoundError: # pragma: no cover
        raise click.ClickException("gcloud not installed. Please install and try again.")
    except subprocess.CalledProcessError as e: # pragma: no cover
        raise click.ClickException(f"Error executing gcloud command: {e.stderr}")
    except json.JSONDecodeError as e: # pragma: no cover
        raise click.ClickException(f"Error decoding JSON: {e.msg}")
    except Exception as e: # pragma: no cover
        raise click.ClickException(f"An unexpected error occurred: {e}")
    

def select_image_from_list(images_data):
    """Allows user to select an image from the list.

    Args:
        images_data (list): A list of dictionaries containing image data.

    Returns:
        str: The selected image tag.
    """
    click.secho("Available Images (Newest to Oldest):", fg="green")
    image_choices = []

    for i, image in enumerate(images_data):
        tag = image.get("tag").split("tags/")[-1]
        image_choices.append(tag)
        click.secho(f"{len(image_choices)}. {tag}", fg="cyan")

    while True:
        try:
            selection = int(input("Select an image (enter number): "))
            if 1 <= selection <= len(image_choices):
                selected_tag = image_choices[selection - 1]
                return selected_tag
            else: # pragma: no cover
                click.secho("Invalid selection. Please enter a number from the list.", fg="red")
        except ValueError: # pragma: no cover
            click.secho("Invalid input. Please enter a number.", fg="red")


def check_for_latest_image(images_data, current_version):
    """Checks if a newer image is available and prompts the user.

    Args:
        images_data (list): A list of dictionaries containing image data.
        current_version (str): The current image version.

    Returns:
        str: The latest image tag if the user chooses to use it, otherwise the current version.
    """

    if images_data:
        latest_image = images_data[0]
        latest_tag = latest_image.get("tag", '').split('tags/')[-1]

        if latest_tag and current_version != latest_tag:
            if ask_user(f"There is a newer image available: {latest_tag}. Would you like to use it?"):
                click.secho("Warning: your airflow db may not be compatible with the newer image.\nUpgrade using `airflow db migrate`.", fg='yellow')
                return latest_tag
            else: # pragma: no cover
                click.secho(f"Using image version: {current_version}", fg="yellow")
        elif latest_tag is None: # pragma: no cover
            click.secho("Could not determine the latest image tag.", fg="yellow")
        else: # pragma: no cover
            click.secho(f"Already using the newest image.", fg="green")
    else:
        click.secho("No images found in the repository.", fg="yellow")
    return current_version # Return the original image_version if no update