from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def place_main():
    if request.method=="POST":
        resp = request.form
        dist1 = resp.get('d1')
        dist1 = dist1.lower()
        tal1 = resp.get('t1')
        tal1 = tal1.lower()
        dist2 = resp.get('d2')
        dist2 = dist2.lower()
        tal2 = resp.get('t2')
        tal2 = tal2.lower()
        result = 0

        if (dist1 == dist2):
            result = "They are from same District"


            if (tal1 == tal2):
                result = "They are from same city as well as Taluka"
            else:
                result = "They are from same city but diff taluka"
        else:
            result = "They are not from same city"

        return render_template("result.html", abc=result, d1=dist1, d2=dist2, t1=tal1, t2=tal2)

    else:
        return render_template("input.html")


if __name__ == '__main__':
    app.run(debug=True)
