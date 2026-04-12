use enigo::{
    Button, Coordinate, Direction, Enigo, Key, Keyboard, Mouse, Settings,
};
use serde::Deserialize;
use std::env;
use std::fs;
use std::path::PathBuf;
use std::process;
use std::thread;
use std::time::Duration;

#[derive(Deserialize, Debug)]
struct Action {
    #[serde(rename = "type")]
    action_type: String,

    #[serde(default)]
    x: i32,
    #[serde(default)]
    y: i32,

    #[serde(default)]
    text: String,

    #[serde(default = "default_delay")]
    delay: f64,
}

#[derive(Deserialize, Debug)]
struct Workflow {
    repetitions: Option<u32>,
    actions: Vec<Action>,
}

fn default_delay() -> f64 {
    1.0
}

fn main() {
    println!("🚀 Rust Legacy Autoclicker (enigo 0.6)");

    let workflow = load_workflow();
    let repetitions = workflow.repetitions.unwrap_or(1);
    let actions = workflow.actions;

    println!("✅ Loaded {} actions × {} repetitions", actions.len(), repetitions);

    let mut enigo = Enigo::new(&Settings::default()).expect("Failed to initialize Enigo");

    println!("\nPress ENTER to START (Ctrl+C to stop)...");
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();

    for rep in 1..=repetitions {
        println!("\n🔄 Repetition {}/{}", rep, repetitions);

        for action in &actions {
            if let Err(e) = execute_action(&mut enigo, action, rep) {
                eprintln!("❌ Error: {}", e);
                process::exit(1);
            }
        }
    }

    println!("\n✅ Automation completed successfully!");
}

fn execute_action(enigo: &mut Enigo, action: &Action, rep: u32) -> Result<(), String> {
    match action.action_type.as_str() {
        "click" => {
            // Move and click
            enigo
                .move_mouse(action.x, action.y, Coordinate::Abs)
                .map_err(|e| e.to_string())?;
            enigo
                .button(Button::Left, Direction::Click)
                .map_err(|e| e.to_string())?;

            println!("✅ Clicked at ({}, {})", action.x, action.y);
        }
        "type" => {
            let final_text = action.text.replace("{rep}", &rep.to_string());
            enigo.text(&final_text).map_err(|e| e.to_string())?;
            println!("✅ Typed: {}", final_text);
        }
        _ => println!("⚠️ Unknown action type: {}", action.action_type),
    }

    thread::sleep(Duration::from_secs_f64(action.delay));
    Ok(())
}

// ====================== WORKFLOW LOADING ======================
fn load_workflow() -> Workflow {
    // 1. From command line argument
    if let Some(arg) = env::args().nth(1) {
        if let Ok(w) = load_file(&PathBuf::from(arg)) {
            return w;
        }
    }

    // 2. Default workflow.json
    if let Ok(mut path) = env::current_exe() {
        path.pop();
        path.push("workflow.json");
        if let Ok(w) = load_file(&path) {
            return w;
        }
    }

    // 3. Ask user interactively
    println!("\n❌ workflow.json not found.");
    loop {
        println!("Enter full path to workflow JSON file (or press Enter to exit):");
        let mut input = String::new();
        std::io::stdin().read_line(&mut input).unwrap();
        let trimmed = input.trim();

        if trimmed.is_empty() {
            println!("Cancelled.");
            process::exit(0);
        }

        let path = PathBuf::from(trimmed);
        if let Ok(w) = load_file(&path) {
            return w;
        }
    }
}

fn load_file(path: &PathBuf) -> Result<Workflow, String> {
    if !path.exists() {
        return Err(format!("File not found: {}", path.display()));
    }

    let content = fs::read_to_string(path).map_err(|e| e.to_string())?;
    let workflow: Workflow = serde_json::from_str(&content)
        .map_err(|e| format!("JSON error: {}", e))?;

    println!("✅ Loaded: {}", path.file_name().unwrap().to_string_lossy());
    Ok(workflow)
}