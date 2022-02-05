use actix_session::CookieSession;
use actix_web::{middleware, App, HttpServer};
use actix_files as fs;
use std::env;
use std::io::Result;
use tera::Tera;

mod lib;
mod server;
use server::{index};

use lib::AppData;

#[actix_web::main]
async fn main() -> Result<()> {
    let port = 8000;
    env::set_var("RUST_LOG", "actix_web=error");
    env_logger::init();

    let address = format!("0.0.0.0:{}", port);
    HttpServer::new(move || {
        let templates = Tera::new("templates/**/*").unwrap();

        App::new()
            .wrap(middleware::Logger::default())
            .wrap(CookieSession::signed(&[0; 32]).secure(false))
            .data(AppData { tmpl: templates })
            .service(index)
            .service(fs::Files::new("/static", "./static"))
    })
    .bind(address)?
    .run()
    .await
}
