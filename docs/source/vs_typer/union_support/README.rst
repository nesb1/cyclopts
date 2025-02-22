======================
Union/Optional Support
======================

Currently, Typer does not support :obj:`~typing.Union` type annotations.

.. code-block:: python

   import typer

   typer_app = typer.Typer()

   @typer_app.command()
   def foo(value: Union[int, str] = "default_str"):
       print(f"{type(value)=} {value=}")

   typer_app(["123"])
   # AssertionError: Typer Currently doesn't support Union types


Cyclopts fully supports :obj:`~typing.Union` annotations.
Cyclopt's :ref:`Coercion Rules <Coercion Rules - Union>` iterate left-to-right over the unioned types until a coercion can be performed without error.

.. code-block:: python

   import cyclopts

   cyclopts_app = cyclopts.App()

   @cyclopts_app.default
   def foo(value: Union[int, str] = "default_str"):
       print(f"{type(value)=} {value=}")

   print("Cyclopts:")
   cyclopts_app(["123"])
   # type(value)=<class 'int'> value=123
   cyclopts_app(["bar"])
   # type(value)=<class 'str'> value='bar'

Naturally, Cyclopts also supports :obj:`~typing.Optional` types, since :obj:`~typing.Optional` is syntactic sugar for ``Union[..., None]``.
