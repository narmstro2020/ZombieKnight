package com.example.zombieknight.ui

import androidx.compose.runtime.Composable
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontFamily
import com.example.zombieknight.game.Input
import com.example.zombieknight.game.World

private const val TICK_NANO = 1_000_000_000L / 60
private val GREEN = Color(25, 200, 25);

class GameFonts(val pixel: FontFamily, val title: FontFamily)


@Composable
fun GameScreen(
    world: World,
    input: Input,
    textures: TextureStore,
    font: GameFonts
) {

    var hud by remember { mutableStateOf(world.game.hud()) }

}