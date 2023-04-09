# Docker

## Introduction to Docker

Docker is a containerization platform that allows developers to package and deploy their applications in a portable and scalable way. With Docker, you can build, ship, and run your applications on any platform or infrastructure. In this tutorial, we'll cover the basics of Docker and show you how to get started with it.

## Installing Docker

To get started with Docker, you'll first need to install it on your machine. Docker is available for all major operating systems, including Windows, macOS, and Linux.

### Windows

If you're using Windows, you can download and install Docker Desktop from the official Docker website [here](https://www.docker.com/products/docker-desktop).

### macOS

If you're using macOS, you can download and install Docker Desktop from the official Docker website [here](https://www.docker.com/products/docker-desktop).

### Linux

If you're using Linux, you can follow the instructions for your specific distribution on the official Docker website [here](https://docs.docker.com/engine/install/).

## Running Your First Docker Container

Once you've installed Docker on your machine, you can start running Docker containers.

### Hello World

To run your first Docker container, you can start with the classic "Hello World" example:

```bash
docker run hello-world
```

This command will download the `hello-world` image from Docker Hub (if it doesn't exist locally), and run a container based on that image. The container will print a message to the console and then exit.

### Nginx Web Server

Another common Docker use case is to run a web server. Here's an example of running an Nginx web server in a Docker container:

```bash
docker run -d -p 8080:80 nginx
```

This command will download the `nginx` image from Docker Hub (if it doesn't exist locally), and run a container based on that image. The `-d` flag runs the container in detached mode (in the background), and the `-p` flag maps the host port `8080` to the container port `80`.

## Building Docker Images

Now that you've seen how to run Docker containers, let's move on to building Docker images. Docker images are the building blocks for containers.

### Dockerfile

To create a Docker image, you'll need to define a `Dockerfile`. A `Dockerfile` is a text file that contains instructions for building a Docker image. Here's an example `Dockerfile` for a Node.js application:

```
dockerfile
Copy code
# Use the official Node.js image as the base image FROM node:14-alpine # Set the working directory in the container WORKDIR /app # Copy the package.json and package-lock.json files to the container COPY package*.json ./ # Install the dependencies RUN npm install # Copy the rest of the application files to the container COPY . . # Expose port 3000 for the application EXPOSE 3000 # Start the application CMD ["npm", "start"]
```

### Building the Image

Once you've created your `Dockerfile`, you can build your Docker image with the `docker build` command:

```bash
docker build -t my-node-app .
```

This command will build a Docker image with the tag `my-node-app` using the current directory (`.`) as the build context.

## Running Your Own Docker Image

Now that you've built your own Docker image, you can run a container based on that image.

```bash
docker run -d -p 3000:3000 my-node-app
```

This command will run a container based on the `my-node-app` image, in detached mode (`-d`), and map the host port `3000` to the container port `3000`.

## Pushing Your Docker Image to Docker Hub

Once you've built your Docker image, you can push it to a Docker registry, such as Docker Hub.

### Login to Docker Hub

Before you can push your Docker image to Docker Hub, you'll need to login to your Docker Hub account:

```bash
docker login
```

### Tag Your Docker Image

Next, you'll need to tag your Docker image with your Docker Hub username and the repository name:

```bash
docker tag my-node-app username/my-node-app
```

### Push Your Docker Image

Finally, you can push your Docker image to Docker Hub:

```bash
docker push username/my-node-app
```

## Conclusion

Congratulations! You've now learned the basics of Docker, including running Docker containers, building Docker images, and pushing Docker images to Docker Hub. Docker is a powerful tool that can help you package and deploy your applications in a portable and scalable way. Keep exploring Docker's features to take your containerization skills to the next level.