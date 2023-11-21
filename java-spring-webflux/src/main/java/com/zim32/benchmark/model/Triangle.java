package com.zim32.benchmark.model;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

public class Triangle implements FigureInterface{
    private final int sizeA;
    private final int sizeB;
    private final int sizeC;

    @JsonCreator
    Triangle(@JsonProperty("sizeA") int sizeA, @JsonProperty("sizeB") int sizeB, @JsonProperty("sizeC") int sizeC) {
        this.sizeA = sizeA;
        this.sizeB = sizeB;
        this.sizeC = sizeC;
    }

    @Override
    public String getType() {
        return "triangle";
    }

    @Override
    public double computeArea() {
        double a = sizeA;
        double b = sizeB;
        double c = sizeC;
        var s = (a + b + c) / 2;

        return Math.sqrt(s * (s - a) * (s - b) * (s - c));
    }
}
