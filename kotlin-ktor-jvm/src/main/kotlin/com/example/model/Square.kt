package com.example.model

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlin.math.pow

@Serializable
@SerialName("square")
class Square(
    private val size: Int
): Figure {
    override fun getType(): String {
        return "square";
    }

    override fun computeArea(): Double {
        return size.toDouble().pow(2.0);
    }
}