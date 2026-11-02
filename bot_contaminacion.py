import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print("Bot de contaminación conectado ✅")


# ----------- BIENVENIDA -----------
@bot.command()
async def start(ctx):
    await ctx.send("¡Hola! 🌎 Soy un bot que te enseña sobre la contaminación ambiental.")
    await ctx.send(
        "Estos son mis comandos:\n"
        "`!contaminacion` → Qué es la contaminación\n"
        "`!recicla` → Cómo reciclar\n"
        "`!reutiliza` → Ideas para reutilizar\n"
        "`!tipos` → Tipos de contaminación\n"
        "`!ejemplos` → Casos reales en el mundo\n"
        "`!consejo` → Un consejo al azar\n"
        "`!basura <color>` → Qué va en cada caneca"
    )


# ----------- 1. QUÉ ES LA CONTAMINACIÓN -----------
@bot.command(name="contaminacion")
async def contaminacion(ctx):
    mensaje = """
🌎 CONTAMINACIÓN AMBIENTAL

La contaminación ocurre cuando sustancias dañinas
afectan nuestro medio ambiente (aire, agua y suelo).

🌫️ Aire: humo de carros y fábricas.
💧 Agua: basura y químicos en los ríos.
🗑️ Suelo: residuos y plásticos.

Escribe !tipos para conocer los tipos de contaminación.
"""
    await ctx.send(mensaje)


# ----------- 2. RECICLAR -----------
@bot.command()
async def recicla(ctx):
    mensaje = """
♻️ RECICLAR

Reciclar es transformar los residuos en nuevos productos.

✅ Separa plástico, vidrio, papel y metal.
✅ Lava los envases antes de botarlos.
✅ Aplasta las botellas para ahorrar espacio.
✅ No mezcles residuos limpios con comida.
"""
    await ctx.send(mensaje)


# ----------- 3. REUTILIZAR -----------
@bot.command()
async def reutiliza(ctx):
    mensaje = """
🔄 REUTILIZAR

Reutilizar es darle una segunda vida a las cosas.

💡 Usa frascos de vidrio para guardar alimentos.
💡 Convierte botellas en materas o macetas.
💡 Usa bolsas de tela en vez de plásticas.
💡 Dona la ropa que ya no uses.
"""
    await ctx.send(mensaje)


# ----------- 4. TIPOS DE CONTAMINACIÓN -----------
@bot.command()
async def tipos(ctx):
    mensaje = """
🧪 TIPOS DE CONTAMINACIÓN

🌫️ Del aire: gases de carros, fábricas e incendios.
💧 Del agua: químicos, aceites y basura en ríos y mares.
🗑️ Del suelo: plásticos, pesticidas y residuos.
🔊 Auditiva: ruido excesivo de ciudades y máquinas.
💡 Lumínica: exceso de luces artificiales de noche.
"""
    await ctx.send(mensaje)


# ----------- 5. EJEMPLOS REALES EN EL MUNDO -----------
@bot.command()
async def ejemplos(ctx):
    mensaje = """
🌍 EJEMPLOS DE CONTAMINACIÓN EN EL MUNDO

🇮🇳 India: ciudades como Delhi sufren niveles muy altos
   de smog (aire contaminado) en invierno.

🌊 Océano Pacífico: la "Gran Isla de Basura" es una enorme
   mancha de plásticos flotando en el mar.

🇨🇳 China: zonas industriales con fuerte contaminación del
   aire por fábricas y carbón.

🌳 Amazonas: la deforestación y los incendios afectan
   el "pulmón del planeta".

🇲🇽 Ciudad de México: alta contaminación del aire por
   tráfico y la geografía del valle.

🏭 Río Citarum (Indonesia): uno de los ríos más
   contaminados del mundo por residuos textiles.
"""
    await ctx.send(mensaje)


# ----------- 6. CONSEJO AL AZAR -----------
@bot.command()
async def consejo(ctx):
    consejos = [
        "🌱 Usa una botella reutilizable para reducir el plástico.",
        "🚲 Camina o usa la bici para distancias cortas.",
        "💡 Apaga las luces que no estés usando.",
        "🚿 Cierra la llave mientras te cepillas los dientes.",
        "🛍️ Lleva tus propias bolsas al supermercado.",
        "🔌 Desconecta los aparatos que no uses.",
    ]
    await ctx.send(random.choice(consejos))


# ----------- 7. GUÍA DE CANECAS POR COLOR -----------
@bot.command()
async def basura(ctx, color=None):  # Ejemplo: !basura blanco
    if color is None:
        await ctx.send("Escribe un color: `!basura blanco`, `!basura negro` o `!basura verde`.")
        return

    color = color.lower()
    if color == "blanco":
        await ctx.send("⚪ Blanco: residuos aprovechables como plástico, vidrio, metal, papel y cartón limpios.")
    elif color == "negro":
        await ctx.send("⚫ Negro: residuos no aprovechables, como papel sucio, servilletas o empaques con comida.")
    elif color == "verde":
        await ctx.send("🟢 Verde: residuos orgánicos, como restos de comida y cáscaras.")
    else:
        await ctx.send("No conozco ese color. Prueba con blanco, negro o verde.")
