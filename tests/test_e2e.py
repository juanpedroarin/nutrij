import re, random
from playwright.sync_api import Playwright, sync_playwright, expect


def test_crear_receta(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    #Genero nombres
    numero_random = random.randint(1, 1000)
    nombre_ing1 = "Ingrediente_1_"+str(numero_random)
    unidad_ing1 = "unidad_1_"+str(numero_random)
    prote_ing1 = str(numero_random)
    nombre_ing2 = "Ingrediente_2_"+str(numero_random)
    unidad_ing2 = "unidad_2_"+str(numero_random)
    prote_ing2 = str(numero_random)

    #Crear ingredientes
    page.goto("http://localhost:5000/")
    page.get_by_role("button", name="Crear Ingrediente").click()
    page.get_by_label("Nombre:").click()
    page.get_by_label("Nombre:").fill(nombre_ing1)
    page.get_by_label("Nombre:").press("Tab")
    page.get_by_label("Unidad:").fill(unidad_ing1)
    page.get_by_label("Unidad:").press("Tab")
    page.get_by_label("Prote:").fill(prote_ing1)
    page.get_by_role("button", name="Crear Ingrediente").click()

    page.get_by_label("Nombre:").click()
    page.get_by_label("Nombre:").fill(nombre_ing2)
    page.get_by_label("Nombre:").press("Tab")
    page.get_by_label("Unidad:").fill(unidad_ing2)
    page.get_by_label("Unidad:").press("Tab")
    page.get_by_label("Prote:").fill(prote_ing2)
    page.get_by_role("button", name="Crear Ingrediente").click()
    
    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Ver").click()
    expect(page.locator("#ingredientes-container")).to_contain_text(nombre_ing1)
    expect(page.locator("#ingredientes-container")).to_contain_text(nombre_ing2)
    page.get_by_role("button", name="Menu").click()

    # Crear receta
    nombre_rec = "Receta_"+str(numero_random)
    descripcion_rec = "Descripcion de la receta_"+str(numero_random)

    page.get_by_role("button", name="Crear Receta").click()
    page.get_by_label("Nombre:").click()
    page.get_by_label("Nombre:").fill(nombre_rec)
    page.get_by_label("Descripción:").click()
    page.get_by_label("Descripción:").fill(descripcion_rec)
    page.get_by_role("button", name="Agregar Ingrediente").click()
    page.locator("#ingredientes").select_option({nombre_ing1})
    page.get_by_role("button", name="Agregar Ingrediente").click()
    page.locator("#ingredientes").nth(1).select_option({nombre_ing2})
    page.get_by_role("button", name="Guardar Receta").click()

    page.get_by_role("button", name="Menu").click()
    page.get_by_role("button", name="Ver").click()
    expect(page.locator("#recetas-container")).to_contain_text("{} - {},{}".format(nombre_rec, nombre_ing1, nombre_ing2))

    # ---------------------
    context.close()
    browser.close()

