use actix_session::Session;
use actix_web::{route, web, Error, HttpResponse};
use crate::AppData;
use tera::Context;

pub async fn increment_counter(session: &Session) -> Result<i32, Error> {
    if let Some(count) = session.get::<i32>("counter")? {
        session.set("counter", count + 1)?;
    } else {
        session.set("counter", 1)?;
    }
    let new_count = session.get::<i32>("counter")?.unwrap();

    Ok(new_count)
}

#[route("/", method="GET", method="POST")]
pub async fn index(data: web::Data<AppData>, session: Session) -> Result<HttpResponse, Error> {
    let new_count = increment_counter(&session).await?;
    let mut ctx = Context::new();
    ctx.insert("count", &new_count);
    if new_count >= 50000 {
        ctx.insert("flag", "UiTHack22{Pressing_Really_really_fast_does_the_trick}")
    }
    let rendered = data.tmpl.render("index.html", &ctx).unwrap();

    Ok(HttpResponse::Ok().body(rendered))
}