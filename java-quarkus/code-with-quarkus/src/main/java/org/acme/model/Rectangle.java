package org.acme.model;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

public class Rectangle implements FigureInterface{
    private final int sizeA;
    private final int sizeB;

    @JsonCreator
    Rectangle(@JsonProperty("sizeA") int sizeA, @JsonProperty("sizeB") int sizeB) {
        this.sizeA = sizeA;
        this.sizeB = sizeB;
    }

    @Override
    public String getType() {
        return "rectangle";
    }

    @Override
    public double computeArea() {
        return sizeA * sizeB;
    }
}
