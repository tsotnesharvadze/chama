from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse
import sqlite3
import json
import re

# Create your views here.

regex = re.compile("\s*,\s*")


def index(request):
    return render(request, 'mshiapp/index.html', {

    })


def get_recipes(request):
    query = request.GET.get('query', '')

    if query == '':
        return HttpResponseNotFound("404 Not found")

    query = regex.split(query)
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    q = "SELECT recipes.name as recipe_name, rules, recipe, img, source FROM recipes"
    where = ""
    first = True

    for i in range(len(query)):
        i = str(i)
        q += " INNER JOIN ingredients as in" + i + " ON recipes.id = in" + i + ".recipe_id"
        where += (" WHERE " if first else " AND ") + "in" + i + ".name = ?"
        first = False

    start = int(request.GET.get('start', '0'))
    limit = int(request.GET.get('limit', '10'))
    where += " ORDER BY rules_count LIMIT {}, {}".format(start, limit)

    #return HttpResponse(q + where)

    cursor.execute(q + where, query)
    data = cursor.fetchall()

    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json; charset=utf-8")


def get_ingredients(request):
    query = request.GET.get("query", "").replace('%', '\%')

    if query != "":
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT(name) FROM ingredients WHERE name LIKE ?", (query + '%',))
        ingredients = cursor.fetchall()

        if ingredients is None:
            ingredients = []
    else:
        ingredients = []

    return HttpResponse(json.dumps(ingredients, ensure_ascii=False), content_type="application/json; charset=utf-8")
