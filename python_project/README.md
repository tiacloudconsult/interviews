1. git clone 'interview repo'
2. install python if you don't have it
3. test the geo.py app to see if you can hit 
--> python3 geo.py
4. Write a dockerfile for this app - remember, it is running on port 5000 
5. Build the docker image of this app
6. Create a deployment and service yaml file, so you can deploy it in kubernetes. (deploy in your kind cluster)
7. use the below command to reach your application
--> kubectl port-forward svc/<name_of_your_service> -n namespace 5000:5000
