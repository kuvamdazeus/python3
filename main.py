import re

f = open("input.txt")

content = f.read()

for testimonial in content.split("\n\n"):
    text, by = testimonial.split("\n")
    by = by.replace("[", "").replace("]", "")
    [name, designation, company_name] = by.split(", ")

    print("""
    <div className="col-md-12">
        <div className="card-testimonial text-left">
            <p>
                {}
            </p>
            <span className="client-detail text-white">
                {}, {}, <span className="text-style-2 ">{}</span>
            </span>
        </div>
    </div>
    """.format(text, name, designation, company_name))

    print()