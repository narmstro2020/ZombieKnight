package com.example.zombieknight.game

class Zombie(
    private val platforms: List<Tile>,
    private val portals: List<Portal>,
    minSpeed: Int,
    maxSpeed: Int
) : Entity(Vec2(64f, 64f)) {

    private val kind = listOf("boy", "girl").random()
    private val walkFrames = loadFrames("zombie/$kind/walk", "Walk", 10)
    private val dieFrames = loadFrames("zombie/$kind/dead", "Dead", 10)
    private val riseFrames = dieFrames.reversed()
    private val hitSound = addSound("zombie_hit")
    private val kickSound = addSound("zombie_kick")
    private val portalSound = addSound("portal_sound")

    val direction: Int = listOf(-1, 1).random()
    private val xPosition = (100..(WINDOW_WIDTH.toInt() - 100)).random().toFloat()
    var pos = Vec2(xPosition, -100f)
    private val xVelocity = (minSpeed..maxSpeed).random().toFloat() * direction
    var velocity = Vec2(xVelocity, 0f)
    var isDead = false
    private var animateDeath = false
    var animateRise = false
    private var roundTime = 0
    private var frameCount = 0
    var alive = true

    init {
        flipH = direction == -1
        showTexture(walkFrames[0])
        setBottomLeft(pos)
    }

    fun update() {
        move()
        checkCollisions()
        checkAnimations()
        if(isDead){
            frameCount +=1
            if (frameCount % 60 == 0){
                roundTime += 1
                if (roundTime == RISE_TIME){
                    animateRise = true
                    currentSprite = 0f
                }
            }
        }
    }

    private fun move() {
        if (isDead) return
        animate(walkFrames, 0.5f)
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

    private fun checkAnimations() {
        if(animateDeath){
            if(animate(dieFrames, 0.095f)) {
                currentSprite = (dieFrames.size - 1).toFloat()
                showTexture(dieFrames.last())
                animateDeath = false
            }
        }

        if(animateRise){
            if(animate(riseFrames, 0.095f)){
                animateRise = false
                isDead = false
                frameCount = 0
                roundTime = 0
            }
        }
    }

    fun die() {
        hitSound.play()
        isDead = true
        animateDeath = true
        currentSprite = 0f
    }

    companion object {
        val VERTICAL_ACCELERATION = Vec2(0f, 3f)

        const val RISE_TIME = 2
    }

}