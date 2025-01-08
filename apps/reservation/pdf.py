from six import BytesIO

from weasyprint import HTML


def generate_reservation(user, reservation):
    try:
        output = BytesIO()
        issue_date = reservation.reservation_time.strftime('%Y-%m-%d')

        html = f"""
        <h1>Band qilindi</h1>
        <p>Kimga: {user.phone_number}</p>
        <p>Band qilingan restaran: {reservation.restaurant}</p>
        <p>Sana: {issue_date}</p>
        """
        html_content = HTML(string=html)
        html_content.write_pdf(output)
        output.seek(0)
        return output.getvalue()
    except Exception as e:
        raise RuntimeError(f"Xatolik {str(e)}")