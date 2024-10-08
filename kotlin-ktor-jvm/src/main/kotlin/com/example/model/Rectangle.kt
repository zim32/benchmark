package com.example.model

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("rectangle")
class Rectangle(
    private val sizeA: Int,
    private val sizeB: Int,
): Figure {
    override fun getType(): String {
        return "rectangle";
    }

    override fun computeArea(): Double {
        return sizeA.toDouble() * sizeB.toDouble();
    }
}