# ==============================================================================
# CONFIGURACION GENERAL DEL JUEGO
# ==============================================================================

# --- CONSTANTES DE PANTALLA ---
ALTO = 480
ANCHO = 640
TITULO = 'Proyecto Shooter'

# --- COLORES (Formato RGB) ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACK = (136, 3, 252)
GREEN = (26, 255, 128)

# --- RUTAS DE RECURSOS (IMAGENES) ---
PLAYER_IMG = 'src/Player.png'
ENEMY_IMG = 'src/Ghouls & Raiders/Ghoul.png'
ENEMY1_IMG = 'src/Ghouls & Raiders/Raider.png'
ROCK_IMG = 'src/Armor Super Mutants/Asuper.png'
BACKGROUND_IMG = 'src/Background.png'
BULLET_IMG = "src/Ammo/Flaser.png"  # Buscar una imagen para las balas
DEFEAT_IMG = 'src/GAME OVER.png'
VICTORY_IMG = 'src/VICTORY.png'

# ARCHIVOS DE FUENTES
FONT_FILE = 'src/r_fallouty.ttf'

# ARCHIV>OS DE MUSICA
MUSIC = 'src/Sounds/RAIDER.mp3'
FIRE_SOUND = 'src/Sounds/Laser.mp3'

# --- RUTAS DE RECURSOS (SONIDOS) ---
# (Puedes agregar tus pistas de audio aquí más adelante)

# --- PARAMETROS INICIALES DE PARTIDA ---
vidas = 10
fallos = 0
puntos = 0
balas_disparadas = 0
FPS = 60

# --- BANDERAS DE ESTADO (CONTROL DEL JUEGO) ---
run = True
finish = False
reloading = False