from playwright.sync_api import Page, expect


def test_drag_and_drop(page: Page) -> None:
    page.goto('https://www.qa-practice.com/elements/dragndrop/boxes')
    source = page.locator('#rect-draggable')
    target = page.locator('#rect-droppable')
    source.drag_to(target)
    expect(page.locator('#text-droppable')).to_have_text('Dropped!')

def test_drag_and_drop_manual(page: Page) -> None:
    page.goto('https://www.qa-practice.com/elements/dragndrop/boxes')
    source = page.locator('#rect-draggable')
    target = page.locator('#rect-droppable')
    source.hover()
    page.mouse.down()
    target.hover()
    page.mouse.up()
    expect(page.locator('#text-droppable')).to_have_text('Dropped!')