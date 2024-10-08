package com.example.model

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlin.math.sqrt

@Serializable
@SerialName("triangle")
class Triangle(
    private val sizeA: Int,
    private val sizeB: Int,
    private val sizeC: Int,
): Figure {
    override fun getType(): String {
        return "triangle";
    }

    override fun computeArea(): Double {
        val a = sizeA.toDouble()
        val b = sizeB.toDouble()
        val c = sizeC.toDouble()

        val s = (a + b + c) / 2;

        return sqrt(s * (s - a) * (s - b) * (s - c))
    }
}