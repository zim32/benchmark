package com.example.benchmark.model;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

public class Circle implements FigureInterface{
    private final int diameter;

    @JsonCreator
    Circle(@JsonProperty("diameter") int diameter) {
        this.diameter = diameter;
    }

    @Override
    public String getType() {
        return "circle";
    }

    @Override
    public double computeArea() {
        var r = (double)diameter / 2;
        return Math.PI * Math.pow(r, 2);
    }
}
