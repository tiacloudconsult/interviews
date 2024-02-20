run docker buiild -t python-app -f ./docker/Dockerfile . from the applications directory
This avoids issues with dockerfile COPY command in this situation where the flask server is in a different
directory from the dockerfile