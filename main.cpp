#include <SFML/Graphics.hpp>
#include <SFML/Window.hpp>
#include <imgui.h>
#include <imgui-SFML.h>
#include <string>
#include <map>

int main() {
    sf::RenderWindow window(sf::VideoMode(800, 600), "Search It - GUI (ImGui + SFML)");
    window.setFramerateLimit(60);
    ImGui::SFML::Init(window);

    std::string query;
    std::map<std::string, std::pair<std::string, std::string>> results = {
        {"Wikipedia", {"An apple is a round, edible fruit...",
                       "Wikipedia: An apple is a round, edible fruit produced by an apple tree."}},
        {"Dictionary", {"1: the usually round, red or yellow...",
                        "Dictionary: A round, edible fruit of a small tree."}},
        {"Thesaurus", {"(No preview available)",
                       "Thesaurus: [Simulated synonyms list here]"}}
    };

    bool show_results = false;
    bool show_full_result = false;
    std::string selected_source;
    std::string result_output;

    sf::Clock deltaClock;
    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            ImGui::SFML::ProcessEvent(event);
            if (event.type == sf::Event::Closed) {
                window.close();
            }
        }

        ImGui::SFML::Update(window, deltaClock.restart());

        ImGui::Begin("Search It");
        if (!show_results) {
            ImGui::InputText("Search Query", &query);
            if (ImGui::Button("Search") && !query.empty()) {
                show_results = true;
            }
        } else if (!show_full_result) {
            ImGui::Text("Results for: %s", query.c_str());
            for (const auto& [source, pair] : results) {
                std::string label = source + ": " + pair.first;
                if (ImGui::Button(label.c_str())) {
                    selected_source = source;
                    result_output = pair.second;
                    show_full_result = true;
                }
            }
            if (ImGui::Button("Back")) {
                show_results = false;
            }
        } else {
            ImGui::Text("Full Result from: %s", selected_source.c_str());
            ImGui::TextWrapped("%s", result_output.c_str());
            if (ImGui::Button("Back to Results")) {
                show_full_result = false;
            }
        }
        ImGui::End();

        window.clear(sf::Color(30, 30, 30));
        ImGui::SFML::Render(window);
        window.display();
    }

    ImGui::SFML::Shutdown();
    return 0;
}
