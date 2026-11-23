package com.example.zombieknight.game

import com.example.zombieknight.game.Type.*


class World(val input: Input) {

    val tileMap = Array(ROWS) {
        Array(COLS) { EMPTY }
    }

    val tiles = mutableListOf<Tile>()
    val platforms = mutableListOf<Tile>()
    val portals = mutableListOf<Portal>()
    val bullets = mutableListOf<Bullet>()
    val rubies = mutableListOf<Ruby>()
    val zombies = mutableListOf<Zombie>()
    lateinit var rubyMaker: RubyMaker
    lateinit var player: Player
    val game: Game

    private val background = Assets.image("background.png")

    private val screen = Rect(Vec2(0f, 0f), Vec2(Entity.WINDOW_WIDTH, Entity.WINDOW_HEIGHT))

    init {
        makeMap()
        buildLevel()
        game = Game(this, player)
        game.pauseGame("Zombie Knight", "tap or press Enter to Begin", null)
    }

    private fun makeMap() {
        putPlatform(3, 0, 14)
        putPlatform(3, 25, 39)
        putPlatform(8, 11, 28)
        putPlatform(10, 0, 5)
        putPlatform(10, 34, 39)
        putPlatform(15, 0, 15)
        putPlatform(15, 24, 39)
        putPlatform(18, 18, 21)
        fillRow(21, GROUND)
        fillRow(22, DIRT)
        tileMap[3][19] = RUBY_MAKER
        tileMap[17][20] = PLAYER
        tileMap[2][0] = GREEN_PORTAL
        tileMap[2][38] = PURPLE_PORTAL
        tileMap[20][0] = PURPLE_PORTAL
        tileMap[20][38] = GREEN_PORTAL
    }

    private fun buildLevel() {
        for (row in tileMap.indices) {
            for (col in tileMap[row].indices) {
                val pos = Vec2(col * Tile.SIZE.x, row * Tile.SIZE.y)
                when (val type = tileMap[row][col]) {
                    EMPTY -> {}
                    DIRT, GROUND, LEFT_PLATFORM, CENTER_PLATFORM, RIGHT_PLATFORM ->
                        addTile(pos, type)

                    RUBY_MAKER -> rubyMaker = RubyMaker
                    GREEN_PORTAL -> addPortal(pos, "green")
                    PURPLE_PORTAL -> addPortal(pos, "purple")
                    PLAYER -> player = Player(pos + Vec2(-32f, 32f), platforms, portals, input)
                }
            }
        }
    }

    private fun putPlatform(row: Int, first: Int, last: Int) {
        for (col in first..last) tileMap[row][col] = CENTER_PLATFORM
        if (first > 0) tileMap[row][first] = LEFT_PLATFORM
        if (last < COLS - 1) tileMap[row][last] = RIGHT_PLATFORM
    }

    private fun fillRow(row: Int, type: Type) {
        for (col in 0..<COLS) tileMap[row][col] = type
    }

    private fun addTile(pos: Vec2, type: Type) {
        val tile = Tile(pos, type)
        tiles.add(tile)
        if (tile.isPlatform) platforms.add(tile)
    }

    private fun addPortal(pos: Vec2, color: String) {
        portals.add(Portal(pos, color))
    }

    fun spawnZombie(minSpeed: Int, maxSpeed: Int) {
        zombies.add(Zombie(platforms, portals, minSpeed, maxSpeed))
    }

    fun spawnRuby() {
        rubies.add(Ruby(platforms, portals))
    }

    fun spawnBullet(b: Bullet) {
        bullets.add(b)
    }

    fun clearAll() {
        zombies.clear()
        bullets.clear()
        rubies.clear()
    }

    fun draw(surface: Surface) {
        drawLevel(surface)
        drawActors(surface)
    }

    fun drawLevel(surface: Surface) {
        surface.drawImage(background, screen, false)
        for (t in tiles) t.draw(surface)
    }

    fun drawActors(surface: Surface) {
        rubyMaker.draw(surface)
        for (p in portals) p.draw(surface)
        player.draw(surface)
        for (b in bullets) b.draw(surface)
        for (z in zombies) z.draw(surface)
        for (r in rubies) r.draw(surface)
    }

    fun step() {
        if (game.paused) {
            if (input.justPressed(Action.ACCEPT)) game.resume()
            input.endTick()
            return
        }
        if (input.justPressed(Action.JUMP)) player.jump()
        if (input.justPressed(Action.FIRE)) spawnBullet(player.fire())

        rubyMaker.update()
        for (p in portals) p.update()
        player.update()
        for (b in bullets) b.update()
        for (z in zombies) z.update()
        for (r in rubies) r.update()
        game.update()

        bullets.removeAll { !it.alive }
        zombies.removeAll { !it.alive }
        rubies.removeAll { !it.alive }
        input.endTick()

    }


    companion object {
        const val ROWS = 23
        const val COLS = 40
    }

}