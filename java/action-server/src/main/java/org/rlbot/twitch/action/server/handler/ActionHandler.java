package org.rlbot.twitch.action.server.handler;

import org.rlbot.twitch.action.server.model.ActionChoice;
import org.rlbot.twitch.action.server.model.AvailableActions;
import org.rlbot.twitch.action.server.model.ModelApiResponse;

import java.util.List;

public interface ActionHandler {
    ModelApiResponse handleActionChoice(ActionChoice choice);
    List<AvailableActions> getActionsCurrentlyAvailable();
}
