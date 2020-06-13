package org.rlbot.twitch.action.server.invoker;

import org.rlbot.twitch.action.server.api.handler.StandardActionHandler;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.ExitCodeGenerator;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;
import springfox.documentation.swagger2.annotations.EnableSwagger2;

/**
 * This class should only be used as an example of how to start the spring application.
 * Bots and scripts should probably start this up in a thread.
 */
@SpringBootApplication
@EnableSwagger2
@ComponentScan(basePackages = { "org.rlbot.twitch.action.server.invoker", "org.rlbot.twitch.action.server.api" , "io.swagger.configuration"})
public class Swagger2SpringBoot implements CommandLineRunner {

    @Override
    public void run(String... arg0) throws Exception {
        if (arg0.length > 0 && arg0[0].equals("exitcode")) {
            throw new ExitException();
        }
    }

    public static void main(String[] args) throws Exception {
        StandardActionHandler.registerActionEntity("testEntity", new TestEntity());
        // This will run on a port specified by server.port in a command line argument or
        // application.properties file. See https://www.baeldung.com/spring-boot-change-port
        new SpringApplication(Swagger2SpringBoot.class).run(args);
    }

    class ExitException extends RuntimeException implements ExitCodeGenerator {
        private static final long serialVersionUID = 1L;

        @Override
        public int getExitCode() {
            return 10;
        }

    }
}
