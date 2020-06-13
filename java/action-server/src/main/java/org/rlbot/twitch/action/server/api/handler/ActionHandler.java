package org.rlbot.twitch.action.server.api.handler;

import org.rlbot.twitch.action.server.model.ActionChoice;
import org.rlbot.twitch.action.server.model.AvailableActions;
import org.rlbot.twitch.action.server.model.ModelApiResponse;

import java.util.List;

/**
 * This is responsible for routing actions to multiple different entities,
 * e.g. you may be running multiple bot instances.
 */
public interface ActionHandler {
    ModelApiResponse handleActionChoice(ActionChoice choice);
    List<AvailableActions> getActionsCurrentlyAvailable();
}
