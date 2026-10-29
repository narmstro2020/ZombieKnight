package com.example.zombieknight.game

class Vec2(var x: Float, var y: Float) {
    operator fun plus(other: Vec2) = Vec2(x + other.x, y + other.y)
    operator fun minus(other: Vec2) = Vec2(x - other.x, y - other.y)
    operator fun unaryMinus() = Vec2(-x, -y)
    operator fun times(k: Float) = Vec2(x * k, y * k)
    override fun toString() = "($x, $y)"
}

operator fun Float.times(v: Vec2) = Vec2(v.x * this, v.y * this)