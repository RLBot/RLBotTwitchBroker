package org.rlbot.twitch.action.server.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonValue;
import org.springframework.validation.annotation.Validated;
import javax.validation.Valid;
import javax.validation.constraints.*;

import com.fasterxml.jackson.annotation.JsonCreator;

/**
 * Gets or Sets StrategicCategory
 */
public enum StrategicCategory {
  NEUTRAL("neutral"),
    OFFENSE("offense"),
    DEFENSE("defense");

  private String value;

  StrategicCategory(String value) {
    this.value = value;
  }

  @Override
  @JsonValue
  public String toString() {
    return String.valueOf(value);
  }

  @JsonCreator
  public static StrategicCategory fromValue(String text) {
    for (StrategicCategory b : StrategicCategory.values()) {
      if (String.valueOf(b.value).equals(text)) {
        return b;
      }
    }
    return null;
  }
}
