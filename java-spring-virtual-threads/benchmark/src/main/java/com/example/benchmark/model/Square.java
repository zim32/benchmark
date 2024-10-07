package com.example.benchmark.model;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

public class Square implements FigureInterface {
    private final int size;

    @JsonCreator
    Square(@JsonProperty("size") int size) {
        this.size = size;
    }

    @Override
    public String getType() {
        return "square";
    }

    @Override
    public double computeArea() {
        return Math.pow(size, 2);
    }
}
