package org.rlbot.twitch.action.server.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.util.ArrayList;
import java.util.List;
import org.rlbot.twitch.action.server.model.BotAction;
import org.springframework.validation.annotation.Validated;
import javax.validation.Valid;
import javax.validation.constraints.*;

/**
 * AvailableActions
 */
@Validated
@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2020-06-13T09:00:27.900-07:00[America/Los_Angeles]")
public class AvailableActions   {
  @JsonProperty("entityName")
  private String entityName = null;

  @JsonProperty("currentAction")
  private BotAction currentAction = null;

  @JsonProperty("availableActions")
  @Valid
  private List<BotAction> availableActions = null;

  public AvailableActions entityName(String entityName) {
    this.entityName = entityName;
    return this;
  }

  /**
   * The name of the bot or script that these actions are associated with.
   * @return entityName
  **/
  @ApiModelProperty(example = "SomeBot", value = "The name of the bot or script that these actions are associated with.")
  
    public String getEntityName() {
    return entityName;
  }

  public void setEntityName(String entityName) {
    this.entityName = entityName;
  }

  public AvailableActions currentAction(BotAction currentAction) {
    this.currentAction = currentAction;
    return this;
  }

  /**
   * Get currentAction
   * @return currentAction
  **/
  @ApiModelProperty(value = "")
  
    @Valid
    public BotAction getCurrentAction() {
    return currentAction;
  }

  public void setCurrentAction(BotAction currentAction) {
    this.currentAction = currentAction;
  }

  public AvailableActions availableActions(List<BotAction> availableActions) {
    this.availableActions = availableActions;
    return this;
  }

  public AvailableActions addAvailableActionsItem(BotAction availableActionsItem) {
    if (this.availableActions == null) {
      this.availableActions = new ArrayList<BotAction>();
    }
    this.availableActions.add(availableActionsItem);
    return this;
  }

  /**
   * Get availableActions
   * @return availableActions
  **/
  @ApiModelProperty(value = "")
      @Valid
    public List<BotAction> getAvailableActions() {
    return availableActions;
  }

  public void setAvailableActions(List<BotAction> availableActions) {
    this.availableActions = availableActions;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AvailableActions availableActions = (AvailableActions) o;
    return Objects.equals(this.entityName, availableActions.entityName) &&
        Objects.equals(this.currentAction, availableActions.currentAction) &&
        Objects.equals(this.availableActions, availableActions.availableActions);
  }

  @Override
  public int hashCode() {
    return Objects.hash(entityName, currentAction, availableActions);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AvailableActions {\n");
    
    sb.append("    entityName: ").append(toIndentedString(entityName)).append("\n");
    sb.append("    currentAction: ").append(toIndentedString(currentAction)).append("\n");
    sb.append("    availableActions: ").append(toIndentedString(availableActions)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }
}
