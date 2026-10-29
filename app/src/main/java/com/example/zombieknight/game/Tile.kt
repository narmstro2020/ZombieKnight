package com.example.zombieknight.game

import com.example.zombieknight.game.Type.*

enum class Type {
    EMPTY,
    DIRT,
    GROUND,
    LEFT_PLATFORM,
    CENTER_PLATFORM,
    RIGHT_PLATFORM
}

class Tile(pos: Vec2, val type: Type) :
    Entity(Vec2(32f, 32f)){

    val isPlatform get() = type != DIRT && type != EMPTY

    init {
        showTexture("")
        setTopLeft(pos)
    }

}