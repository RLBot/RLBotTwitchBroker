package org.rlbot.twitch.action.server.api.handler;

import org.rlbot.twitch.action.server.model.BotAction;
import org.rlbot.twitch.action.server.model.ModelApiResponse;

import java.util.List;

/**
 * Bots or scripts should implement this interface if you want to take advantage
 * of the standard action handler.
 */
public interface ActionEntity {
    ModelApiResponse handleActionChoice(BotAction action);
    List<BotAction> getAvailableActions();
    BotAction getCurrentAction();
}
