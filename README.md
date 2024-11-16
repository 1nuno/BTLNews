
#  ByTheLaw News

This is a web project that provides a more user-friendly interface to the Diário da República (the official gazette of Portugal) data. The project aims to make it easier for users to search, view, and interact with legal documents and announcements published by the Portuguese government.

## Prerequisites

Ensure you have Docker, Docker Compose, and Make installed on your system:

- **Docker**: Download and install from [Docker's official website](https://www.docker.com/get-started).
- **Docker Compose**: Usually bundled with Docker Desktop. Verify installation with:
  ```bash
  docker-compose --version
  ```
- **Make**: Make is often pre-installed on Unix-based systems. To check if it's available, run:

  ```bash
  make --version
  ```
  > If `make` is not installed, you can install it via your package manager. For example, on Ubuntu:
    ```bash
    sudo apt-get install make
    ```
  > For Windows, you may need to install Make via a compatible tool like [Chocolatey](https://chocolatey.org/) or use WSL (Windows Subsystem for Linux).

## Getting Started

Follow these steps to set up and run the project from scratch.

### 0. Configure SSH Keys (Optional but Recommended)

SSH Key will enable secure and efficient access to your GitLab repository. To generate and add an SSH key, follow these steps:

1. **Generate an SSH Key**:
  ```bash
  ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
  ```
  Follow the prompts to save the key to the default location and set a passphrase.

2. **Add the SSH Key to the SSH Agent**:
  ```bash
  eval "$(ssh-agent -s)"
  ssh-add ~/.ssh/id_rsa
  ```

3. **Add the SSH Key to Your GitLab Account**:
  > Copy the SSH key to your clipboard:

  ```bash
    cat ~/.ssh/id_rsa.pub
  ```

  > Go to your GitLab account, navigate to **Settings > SSH Keys**, and paste the key.

Using SSH keys enhances security and avoids the need to enter your username and password for each Git operation.

>You can check the documentation [here](https://docs.gitlab.com/ee/user/ssh.html) for more information.

### 1. Clone the Repository

If you have doubts on this step, check out the documentation [here](https://docs.gitlab.com/ee/topics/git/clone.html).

With SSH:

```bash
git clone git@gitlab.com:JohnyPeters/by-the-law.git
cd by-the-law
```

With HTTPs:

```bash
git clone https://gitlab.com/JohnyPeters/by-the-law.git
cd by-the-law
```


### 2. Set Up Environment Variables

Create a `.env` file in the root directory to configure database credentials and Django settings:

```plaintext
POSTGRES_NAME=postgres
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
DJANGO_SUPERUSER_USERNAME=root
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=admin
```

You can also use the commend and update your variables:
```bash
cp .env.example .env
```

> In order to run locally you can just update  
  **DJANGO_SUPERUSER_USERNAME**, **DJANGO_SUPERUSER_EMAIL** and **DJANGO_SUPERUSER_PASSWORD**.


### 3. Build and Run the Project

Use Docker Compose to build and start the project:

```bash
make start
```

> If it is the first time you are running the project or whenever you see some warning like:
  ```bash
  You have X unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
  ```
  You can just run:
  ```bash
  make migrate
  ```

And finally:

```bash
make runserver
```

- This command builds and starts the containers in detached mode, setting up the database and web services.
- In the first run it will also migrate the database, create a superuser with your env settings

### 4. Access the Application

The application should be accessible at [http://localhost:8000](http://localhost:8000).
The application admin should be accessible at [http://localhost:8000/admin](http://localhost:8000/admin)

### 3. Stopping the Project Without Data Loss

To stop the project without removing data, press Ctrl + C, and then:

```bash
make stop
```
If you forget doing that the containers will keep up on the background of your system.


## Other useful commands (no need to run any of these):

### Linting your file changes

After work on some code changes you should run:

```bash
make lint
```
That will point something wrong on the organization of your code. Before opening a new Merge Request make sure to run this.

### Load Original Data into Postgress

If it is the first time you are running this project or you didn't have loaded the data yet, you should download the sqlite file from our [google drive](https://drive.google.com/file/d/1qCVdBCpu80rOqPVud5ks__Vg54kCv1Hx/view?usp=drive_link) and add extract it to the right folder like the following path:

```bash
  by-the-law/apps/dre/migrations/data/2024-10-27-DRE.sqlite3
```

If you try to migrate before this migration will fail, since it will not find the right path.


### Migrate the Database

After the containers are up, apply migrations to set up the database schema:

```bash
make migrate
```

### Create a Superuser

By default the superuser will be created using your variables: To access the Django admin interface, create a superuser account:

```bash
make createsuperuser
```

Follow the prompts to set up an admin account.

### Open server Bash

This command opens a bash shell inside the running web container, allowing you to interact with the application environment directly.

```bash
make bash
```

### [WARNING] Remove all containers 

If you wish to **REMOVE** all containers and volumes (and thus the data), use:

  ```bash
  make remove
  ```

## Additional Commands

You can use `make help` to see a list of all available Make commands.

In case you don't have make installed you can check for the commands in the [Makefile](./Makefile)