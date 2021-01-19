from flask import redirect, render_template, request, session

""" Helpful custom functions created by your friendly neighborhood P4-Tide """


def apology(message, code=400):
    """Render message as an apology to user when errors occur."""
    return render_template("apology.html", code=code, message=message)