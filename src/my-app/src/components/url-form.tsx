"use client";

import { useState } from "react";
import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import * as z from "zod";
import axios from "axios";

import { Button } from "@/components/ui/button";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";

const formSchema = z.object({
  websiteUrl: z.string(),
});

const UrlForm = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      websiteUrl: "",
    },
  });

  async function onSubmit(values: z.infer<typeof formSchema>) {
    try {
      setLoading(true);
      setError(null);

      const response = await axios.post("/api/scrap", {
        url: values.websiteUrl,
      });

      if (response.status === 200) {
        const data = response.data;
        console.log(data.message);
      } else {
        console.error("Image scraping failed");
        setError("Image scraping failed. Please try again.");
      }
    } catch (error) {
      console.error("An error occurred:", error);
      setError(`An error occurred: ${error.message}`);
    } finally {
      setLoading(false);
    }
  }

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
        <h1 className="text-custom-green-dark font-montserrat text-[22px] font-extrabold">
          Image Scrapping
        </h1>
        <FormField
          control={form.control}
          name="websiteUrl"
          render={({ field }) => (
            <FormItem>
              <FormControl className="bg-gray-300">
                <Input placeholder="Website URL" {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        <Button
          type="submit"
          variant="outline"
          className="text-white bg-custom-black font-semibold rounded-xl px-5"
          disabled={loading}
        >
          {loading ? "Loading..." : "SUBMIT"}
        </Button>
        {error && (
          <p className="text-red-500 mt-2">
            <strong>Error:</strong> {error}
          </p>
        )}
      </form>
    </Form>
  );
};

export default UrlForm;
