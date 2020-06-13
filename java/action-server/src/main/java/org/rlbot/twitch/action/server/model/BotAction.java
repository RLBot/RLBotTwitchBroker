package org.rlbot.twitch.action.server.model;

import java.util.Objects;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonCreator;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.rlbot.twitch.action.server.model.StrategicCategory;
import org.springframework.validation.annotation.Validated;
import javax.validation.Valid;
import javax.validation.constraints.*;

/**
 * BotAction
 */
@Validated
@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.SpringCodegen", date = "2020-06-13T09:35:18.293-07:00[America/Los_Angeles]")
public class BotAction   {
  @JsonProperty("description")
  private String description = null;

  @JsonProperty("actionType")
  private String actionType = null;

  @JsonProperty("strategicCategory")
  private StrategicCategory strategicCategory = null;

  @JsonProperty("data")
  @Valid
  private Map<String, Object> data = null;

  public BotAction description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Get description
   * @return description
  **/
  @ApiModelProperty(example = "Demolish enemy bot named SomeBot", value = "")
  
    public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }

  public BotAction actionType(String actionType) {
    this.actionType = actionType;
    return this;
  }

  /**
   * Get actionType
   * @return actionType
  **/
  @ApiModelProperty(example = "demolishEnemy", required = true, value = "")
      @NotNull

    public String getActionType() {
    return actionType;
  }

  public void setActionType(String actionType) {
    this.actionType = actionType;
  }

  public BotAction strategicCategory(StrategicCategory strategicCategory) {
    this.strategicCategory = strategicCategory;
    return this;
  }

  /**
   * Get strategicCategory
   * @return strategicCategory
  **/
  @ApiModelProperty(value = "")
  
    @Valid
    public StrategicCategory getStrategicCategory() {
    return strategicCategory;
  }

  public void setStrategicCategory(StrategicCategory strategicCategory) {
    this.strategicCategory = strategicCategory;
  }

  public BotAction data(Map<String, Object> data) {
    this.data = data;
    return this;
  }

  public BotAction putDataItem(String key, Object dataItem) {
    if (this.data == null) {
      this.data = new HashMap<String, Object>();
    }
    this.data.put(key, dataItem);
    return this;
  }

  /**
   * Get data
   * @return data
  **/
  @ApiModelProperty(value = "")
  
    public Map<String, Object> getData() {
    return data;
  }

  public void setData(Map<String, Object> data) {
    this.data = data;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BotAction botAction = (BotAction) o;
    return Objects.equals(this.description, botAction.description) &&
        Objects.equals(this.actionType, botAction.actionType) &&
        Objects.equals(this.strategicCategory, botAction.strategicCategory) &&
        Objects.equals(this.data, botAction.data);
  }

  @Override
  public int hashCode() {
    return Objects.hash(description, actionType, strategicCategory, data);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BotAction {\n");
    
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    actionType: ").append(toIndentedString(actionType)).append("\n");
    sb.append("    strategicCategory: ").append(toIndentedString(strategicCategory)).append("\n");
    sb.append("    data: ").append(toIndentedString(data)).append("\n");
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
