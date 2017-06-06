# jinja2-passlib_hash-filter

Jinja2 Extension for Password hash generation using passlib


Usage

The extension comes with a passlib_hash tag that provides sha512 hash for function from your templates.

Intended to be used in cookiecutter to generare password hash

.. code-block:: python

  clusluster_product/infra/cookiecutter.json
  {
  "_extensions"                              :  ["jinja2_passlib_hash.Passlib_ext"]
  }

  cluster_product/infra/{{ cookiecutter.cluster_name }}/infra/config.yml
  
  salt_api_password_hash: "{{ cookiecutter.salt_api_password|passlib_hash }}"
