package com.example.zombieknight.game

class Ruby(
    private val platforms: List<Tile>,
    private val portals: List<Portal>
) : Entity(Vec2(64f, 64f)) {


    private val frames = loadTiles("ruby", 7)
    private val portalSound = addSound("portal_sound")

    var pos = Vec2(WINDOW_WIDTH / 2, 100f)
    var velocity = listOf(-HORIZONTAL_VELOCITY, HORIZONTAL_VELOCITY).random()
    var alive = true

    init {
        showTexture(frames[0])
        setBottomLeft(pos)
    }

    fun update() {
        animate(frames, 0.25f)
        move()
        checkCollisions()
    }

    fun move() {
        velocity += VERTICAL_ACCELERATION
        pos += velocity + 0.5f * VERTICAL_ACCELERATION
        if (pos.x < 0) pos.x = WINDOW_WIDTH
        else if (pos.x > WINDOW_WIDTH) pos.x = 0f
        setBottomLeft(pos)
    }

    fun checkCollisions() {
        for (t in platforms) {
            if (rect.intersects(t.rect)) {
                pos.y = t.rect.pos.y + 1
                velocity.y = 0f
                setBottomLeft(pos)
                break
            }
        }

        for (p in portals) {
            if (rect.intersects(p.rect)) {
                portalSound.play()
                pos.x = if (pos.x > WINDOW_WIDTH / 2) 86f else WINDOW_WIDTH - 150
                pos.y = if (pos.y > WINDOW_HEIGHT / 2) 64f else WINDOW_HEIGHT - 132
                setBottomLeft(pos)
                break
            }
        }
    }


    companion object {
        val VERTICAL_ACCELERATION = Vec2(0f, 3f) // gravity
        val HORIZONTAL_VELOCITY = Vec2(5f, 0f)
    }

}