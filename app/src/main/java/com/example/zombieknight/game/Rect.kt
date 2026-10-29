package com.example.zombieknight.game

/** Where something is and how big is it.  position is top left corner. */
class Rect(var pos: Vec2, var size: Vec2) {
    val right get() = pos.x + size.x
    val left get() = pos.x
    val top get() = pos.y
    val bottom get() = pos.y + size.y

    fun intersects(other: Rect): Boolean {
        val check1 = left < other.right
        val check2 = right > other.left
        val check3 = top < other.bottom
        val check4 = bottom > other.top
        return check1 && check2 && check3 && check4
    }

    override fun toString(): String {
        return "Rect($pos.x, $pos.y, $size.x, $size.y)"
    }
}