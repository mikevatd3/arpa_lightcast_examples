# ARPA Lightcast Example Calls

A collection of example scripts calling the Lightcast API, roughly outlining how
data is assembled in the ARPA `detroit_tech_employment` database.

Check out [this document](lightcast_basics.md) to learn more about the datasets that are available.


## Installing

This uses [uv](https://docs.astral.sh/uv/getting-started/installation/) for package management.

Once you have uv installed -- run `uv sync` to install all dependencies.


## Setting up auth

Create a json file with your API username and secret and save it as `config.json` the root folder of this project.

Like this:

```
{
    "username": "useruseruser",
    "secret": "passworddrowssap"
}
```

**Don't stress, it's gitignored.**

## API scripts

Several example scripts live in 'examples.' There are example calls for both the 'metadata' and 'data' endpoints for each service we have access to.

