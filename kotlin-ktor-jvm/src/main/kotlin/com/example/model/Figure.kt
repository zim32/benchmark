package com.example.model

import kotlinx.serialization.Serializable

@Serializable
sealed interface Figure {
    fun getType(): String;
    fun computeArea(): Double;
}