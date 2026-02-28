import datetime

def generate_report(target, findings):
    filename = f"reports/report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.html"

    with open(filename, "w") as f:
        f.write("<html><body style='background:#111;color:#eee;font-family:Arial;'>")
        f.write(f"<h1 style='color:red;'>VulnEye Pro Report</h1>")
        f.write(f"<p><strong>Target:</strong> {target}</p>")
        f.write("<hr>")

        if not findings:
            f.write("<p style='color:lime;'>No major issues detected.</p>")
        else:
            for finding in findings:
                f.write("<div style='margin-bottom:20px;'>")
                f.write(f"<h3 style='color:orange;'>{finding['title']}</h3>")
                f.write(f"<p><strong>Severity:</strong> {finding['severity']}</p>")
                f.write(f"<p><strong>OWASP:</strong> {finding['owasp']}</p>")
                f.write(f"<p><strong>Evidence:</strong> {finding['evidence']}</p>")
                f.write("</div>")

        f.write("</body></html>")

    return filename
