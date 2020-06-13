package org.rlbot.twitch.action.server.api;

import org.rlbot.twitch.action.server.model.ActionChoice;
import org.rlbot.twitch.action.server.model.AvailableActions;
import org.rlbot.twitch.action.server.model.ModelApiResponse;
import com.fasterxml.jackson.databind.ObjectMapper;
import io.swagger.annotations.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CookieValue;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RequestPart;
import org.springframework.web.multipart.MultipartFile;

import javax.validation.constraints.*;
import javax.validation.Valid;
import javax.servlet.http.HttpServletRequest;
import java.io.IOException;
import java.util.List;
import java.util.Map;
@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2020-06-13T09:35:18.293-07:00[America/Los_Angeles]")
@Controller
public class ActionApiController implements ActionApi {

    private static final Logger log = LoggerFactory.getLogger(ActionApiController.class);

    private final ObjectMapper objectMapper;

    private final HttpServletRequest request;

    @org.springframework.beans.factory.annotation.Autowired
    public ActionApiController(ObjectMapper objectMapper, HttpServletRequest request) {
        this.objectMapper = objectMapper;
        this.request = request;
    }

    public ResponseEntity<ModelApiResponse> chooseAction(@ApiParam(value = "Action to choose" ,required=true )  @Valid @RequestBody ActionChoice body
) {
        String accept = request.getHeader("Accept");
        if (accept != null && accept.contains("application/json")) {
            try {
                return new ResponseEntity<ModelApiResponse>(objectMapper.readValue("{\r\n  \"code\" : 200,\r\n  \"message\" : \"Succesfully processed operation\"\r\n}", ModelApiResponse.class), HttpStatus.NOT_IMPLEMENTED);
            } catch (IOException e) {
                log.error("Couldn't serialize response for content type application/json", e);
                return new ResponseEntity<ModelApiResponse>(HttpStatus.INTERNAL_SERVER_ERROR);
            }
        }

        return new ResponseEntity<ModelApiResponse>(HttpStatus.NOT_IMPLEMENTED);
    }

    public ResponseEntity<List<AvailableActions>> getActionsCurrentlyAvailable() {
        String accept = request.getHeader("Accept");
        if (accept != null && accept.contains("application/json")) {
            try {
                return new ResponseEntity<List<AvailableActions>>(objectMapper.readValue("[ {\r\n  \"availableActions\" : [ null, null ],\r\n  \"entityName\" : \"SomeBot\",\r\n  \"currentAction\" : {\r\n    \"actionType\" : \"demolishEnemy\",\r\n    \"data\" : \"\",\r\n    \"description\" : \"Demolish enemy bot named SomeBot\",\r\n    \"strategicCategory\" : \"neutral\"\r\n  }\r\n}, {\r\n  \"availableActions\" : [ null, null ],\r\n  \"entityName\" : \"SomeBot\",\r\n  \"currentAction\" : {\r\n    \"actionType\" : \"demolishEnemy\",\r\n    \"data\" : \"\",\r\n    \"description\" : \"Demolish enemy bot named SomeBot\",\r\n    \"strategicCategory\" : \"neutral\"\r\n  }\r\n} ]", List.class), HttpStatus.NOT_IMPLEMENTED);
            } catch (IOException e) {
                log.error("Couldn't serialize response for content type application/json", e);
                return new ResponseEntity<List<AvailableActions>>(HttpStatus.INTERNAL_SERVER_ERROR);
            }
        }

        return new ResponseEntity<List<AvailableActions>>(HttpStatus.NOT_IMPLEMENTED);
    }

}
