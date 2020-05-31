java -jar swagger-codegen-cli-3.0.20.jar generate^
   -i action-swagger.yaml^
   -l python-flask^
   -o swagger\action-server^
   -DpackageName=rlbot_action_server

java -jar swagger-codegen-cli-3.0.20.jar generate^
   -i action-swagger.yaml^
   -l python^
   -o swagger\action-client^
   -DpackageName=rlbot_action_client
