java -jar swagger-codegen-cli-3.0.20.jar generate^
   -i swagger.yaml^
   -l python-flask^
   -o src\server^
   -DpackageName=rlbot_action_server

java -jar swagger-codegen-cli-3.0.20.jar generate^
   -i swagger.yaml^
   -l python^
   -o src\client^
   -DpackageName=rlbot_action_client