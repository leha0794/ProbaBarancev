
// проверка адреса
if wd.current_url.endswith("/group.php"):
    return



// проверка адреса и еще наличие элемента, если адреса одинаковые
if wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0:
    return
