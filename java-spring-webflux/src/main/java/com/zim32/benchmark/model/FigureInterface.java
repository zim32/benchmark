package com.zim32.benchmark.model;

import com.fasterxml.jackson.annotation.JsonSubTypes;
import com.fasterxml.jackson.annotation.JsonTypeInfo;

@JsonTypeInfo(
        use = JsonTypeInfo.Id.NAME,
        include = JsonTypeInfo.As.PROPERTY,
        property = "type"
)
@JsonSubTypes({
        @JsonSubTypes.Type(value = Square.class, name = "square"),
        @JsonSubTypes.Type(value = Rectangle.class, name = "rectangle"),
        @JsonSubTypes.Type(value = Triangle.class, name = "triangle"),
        @JsonSubTypes.Type(value = Circle.class, name = "circle"),
})
public interface FigureInterface {
    public String getType();
    public double computeArea();
}