package org.rlbot.twitch.action.server.api;

import com.fasterxml.jackson.databind.ObjectMapper;
import io.swagger.annotations.ApiParam;
import org.rlbot.twitch.action.server.api.handler.ActionHandler;
import org.rlbot.twitch.action.server.model.ActionChoice;
import org.rlbot.twitch.action.server.model.AvailableActions;
import org.rlbot.twitch.action.server.model.ModelApiResponse;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;

import javax.servlet.http.HttpServletRequest;
import javax.validation.Valid;
import java.util.List;
@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2020-06-13T09:35:18.293-07:00[America/Los_Angeles]")
@Controller
public class ActionApiController implements ActionApi {

    private static final Logger log = LoggerFactory.getLogger(ActionApiController.class);

    private final ObjectMapper objectMapper;

    private final HttpServletRequest request;

    private final ActionHandler actionHandler;

    @org.springframework.beans.factory.annotation.Autowired
    public ActionApiController(ObjectMapper objectMapper, HttpServletRequest request, ActionHandler actionHandler) {
        this.objectMapper = objectMapper;
        this.request = request;
        this.actionHandler = actionHandler;
    }

    public ResponseEntity<ModelApiResponse> chooseAction(@ApiParam(value = "Action to choose" ,required=true )  @Valid @RequestBody ActionChoice body
) {
        try {
            ModelApiResponse modelApiResponse = actionHandler.handleActionChoice(body);
            return new ResponseEntity<ModelApiResponse>(modelApiResponse, HttpStatus.OK);
        } catch (Exception e) {
            log.error("Failed to handle action.", e);
            return new ResponseEntity<ModelApiResponse>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    public ResponseEntity<List<AvailableActions>> getActionsCurrentlyAvailable() {
        try {
            List<AvailableActions> actions = actionHandler.getActionsCurrentlyAvailable();
            return new ResponseEntity<List<AvailableActions>>(actions, HttpStatus.OK);
        } catch (Exception e) {
            log.error("Failed to get actions.", e);
            return new ResponseEntity<List<AvailableActions>>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

}
