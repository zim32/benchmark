package com.example.model

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlin.math.pow

@Serializable
@SerialName("circle")
final class Circle(
    private val diameter: Int
): Figure {
    override fun getType(): String {
        return "circle";
    }

    override fun computeArea(): Double {
        val r = diameter.toDouble() / 2
        return (Math.PI * r.pow(2.0))
    }
}