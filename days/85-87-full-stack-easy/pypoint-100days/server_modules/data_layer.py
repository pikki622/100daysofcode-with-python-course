import tables
from tables import app_tables
import anvil.server
import datetime

@anvil.server.callable
def all_docs():
  return list(
      app_tables.documents.search(tables.order_by("created", ascending=False)))


@anvil.server.callable
def all_categories():
  return list(app_tables.categories.search(tables.order_by("name")))


@anvil.server.callable
def doc_by_name(name):
  return app_tables.documents.get(name=name)


@anvil.server.callable
def category_by_name(category_name):
  return app_tables.categories.get(name=category_name)

@anvil.server.callable
def add_doc(doc_name, category_name, contents, views):
  now = datetime.datetime.now()
  print(
      f"Server: Creating new document: {doc_name} {category_name} {views} {contents}"
  )
  category = category_by_name(category_name)
  app_tables.documents.add_row(name=doc_name, category=category, contents=contents, views=views, created=now)
  return doc_by_name(doc_name)


