package org.rlbot.twitch.action.server.handler;

import org.rlbot.twitch.action.server.model.ActionChoice;
import org.rlbot.twitch.action.server.model.AvailableActions;
import org.rlbot.twitch.action.server.model.ModelApiResponse;

import java.util.List;

public class StandardActionHandler implements ActionHandler {
    @Override
    public ModelApiResponse handleActionChoice(ActionChoice choice) {
        return null;
    }

    @Override
    public List<AvailableActions> getActionsCurrentlyAvailable() {
        return null;
    }
}
