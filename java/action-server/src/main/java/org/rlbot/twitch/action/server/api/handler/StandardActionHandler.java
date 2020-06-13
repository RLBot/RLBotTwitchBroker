package org.rlbot.twitch.action.server.api.handler;

import org.rlbot.twitch.action.server.model.ActionChoice;
import org.rlbot.twitch.action.server.model.AvailableActions;
import org.rlbot.twitch.action.server.model.ModelApiResponse;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.concurrent.ConcurrentHashMap;
import java.util.stream.Collectors;

@Component
public class StandardActionHandler implements ActionHandler {

    private static ConcurrentHashMap<String, ActionEntity> ACTION_ENTITIES = new ConcurrentHashMap<>();

    public static void registerActionEntity(String entityName, ActionEntity entity) {
        ACTION_ENTITIES.put(entityName, entity);
    }

    @Override
    public ModelApiResponse handleActionChoice(ActionChoice choice) {
        ActionEntity actionEntity = ACTION_ENTITIES.get(choice.getEntityName());
        if (actionEntity == null) {
            return new ModelApiResponse()
                    .code(404)
                    .message(String.format("Entity %s was not found.", choice.getEntityName()));
        }

        return actionEntity.handleActionChoice(choice.getAction());
    }

    @Override
    public List<AvailableActions> getActionsCurrentlyAvailable() {
        return ACTION_ENTITIES.entrySet().stream()
                .map(entry -> getAvailableActions(entry.getKey(), entry.getValue()))
                .collect(Collectors.toList());
    }

    private AvailableActions getAvailableActions(String entityName, ActionEntity entity) {
        return new AvailableActions()
                .entityName(entityName)
                .currentAction(entity.getCurrentAction())
                .availableActions(entity.getAvailableActions());
    }
}
