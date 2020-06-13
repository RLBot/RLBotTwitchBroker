package org.rlbot.twitch.action.server.invoker;

import org.rlbot.twitch.action.server.api.handler.ActionEntity;
import org.rlbot.twitch.action.server.model.BotAction;
import org.rlbot.twitch.action.server.model.ModelApiResponse;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Arrays;
import java.util.List;

public class TestEntity implements ActionEntity {

    private static final Logger log = LoggerFactory.getLogger(TestEntity.class);

    @Override
    public ModelApiResponse handleActionChoice(BotAction action) {
        log.info("Handling action {}", action.getDescription());
        return new ModelApiResponse().code(200).message("Will do");
    }

    @Override
    public List<BotAction> getAvailableActions() {
        return Arrays.asList(new BotAction().description("Let's go"));
    }

    @Override
    public BotAction getCurrentAction() {
        return null;
    }
}
