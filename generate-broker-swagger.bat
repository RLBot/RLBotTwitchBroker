java -jar swagger-codegen-cli-3.0.20.jar generate^
   -i broker-swagger.yaml^
   -l python-flask^
   -o swagger\broker-server^
   -DpackageName=rlbot_twitch_broker_server

java -jar swagger-codegen-cli-3.0.20.jar generate^
   -i broker-swagger.yaml^
   -l python^
   -o swagger\broker-client^
   -DpackageName=rlbot_twitch_broker_client
